// Функция ymaps.ready() будет вызвана, когда
        // загрузятся все компоненты API, а также когда будет готово DOM-дерево.
        ymaps.ready(init);
        let suggestView;
        function init() {
            var myPlacemark;
            suggestViewFrom = new ymaps.SuggestView('id_objectaddress');
            // Создание карты.
            var myMap = new ymaps.Map("map", {
                // Координаты центра карты.
                // Порядок по умолчанию: «широта, долгота».
                // Чтобы не определять координаты центра карты вручную,
                // воспользуйтесь инструментом Определение координат.
                center: [55.76, 37.64],
                // Уровень масштабирования. Допустимые значения:
                // от 0 (весь мир) до 19.
                zoom: 11
            });

            //myMap.geoObjects.add(suggestViewFrom.get());

            id_objectaddress.onchange = function () {
                suggestViewFrom.events.add("select", function (e) {
                    $('#id_objectaddress').empty();
                    const myGeocoder = ymaps.geocode(e.get('item').value);
                    myGeocoder.then(function (res) {
                        var myCoords = res.geoObjects.get(0).geometry.getCoordinates();
                        if (myPlacemark) {
                            myPlacemark.geometry.setCoordinates(myCoords);
                            myMap.panTo(
                                // Координаты нового центра карты
                                myCoords, {
                                flying: true
                            }
                            )
                        }
                        // Если нет – создаем.
                        else {
                            myPlacemark = new createPlacemark(myCoords);
                            myMap.geoObjects.add(myPlacemark);
                            // Слушаем событие окончания перетаскивания на метке.
                            myPlacemark.events.add('dragend', function () {
                                getAddress(myPlacemark.geometry.getCoordinates());
                            });
                            myMap.panTo(
                                // Координаты нового центра карты
                                myCoords, {
                                flying: true
                            }
                            )
                        }
                        getAddress(myCoords);
                    });
                });
            }

            // Слушаем клик на карте.
            myMap.events.add('click', function (e) {
                //$('#id_objectname').empty();
                var coords = e.get('coords');

                // Если метка уже создана – просто передвигаем ее.
                if (myPlacemark) {
                    //$('#id_objectname').empty();
                    myPlacemark.geometry.setCoordinates(coords);
                }
                // Если нет – создаем.
                else {
                    myPlacemark = createPlacemark(coords);
                    myMap.geoObjects.add(myPlacemark);
                    // Слушаем событие окончания перетаскивания на метке.
                    myPlacemark.events.add('dragend', function () {
                        getAddress(myPlacemark.geometry.getCoordinates());
                    });
                }
                getAddress(coords);
            });

            // Создание метки.
            function createPlacemark(coords) {
                return new ymaps.Placemark(coords, {
                    iconCaption: 'поиск...'
                }, {
                    preset: 'islands#violetDotIconWithCaption',
                    draggable: true
                });
            }

            // Определяем адрес по координатам (обратное геокодирование).
            function getAddress(coords) {
                //$('#id_objectname').empty();
                myPlacemark.properties.set('iconCaption', 'поиск...');
                ymaps.geocode(coords).then(function (res) {
                    var firstGeoObject = res.geoObjects.get(0);

                    myPlacemark.properties
                        .set({
                            // Формируем строку с данными об объекте.
                            iconCaption: [
                                // Название населенного пункта или вышестоящее административно-территориальное образование.
                                firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                                // Получаем путь до топонима, если метод вернул null, запрашиваем наименование здания.
                                firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                            ].filter(Boolean).join(', '),
                            // В качестве контента балуна задаем строку с адресом объекта.
                            balloonContent: firstGeoObject.getAddressLine()
                        });
                    var el = firstGeoObject.getAddressLine();
                    console.log(el);
                    //console.log($('#id_objectname').val())
                    $('#id_objectaddress').empty();
                    console.log($('#id_objectaddress').val())
                    $('#id_objectaddress').append(el);
                });
            }
        }
