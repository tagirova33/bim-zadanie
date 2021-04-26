// ������� ymaps.ready() ����� �������, �����
        // ���������� ��� ���������� API, � ����� ����� ����� ������ DOM-������.
        ymaps.ready(init);
        let suggestView;
        function init() {
            var myPlacemark;
            suggestViewFrom = new ymaps.SuggestView('id_objectaddress');
            // �������� �����.
            var myMap = new ymaps.Map("map", {
                // ���������� ������ �����.
                // ������� �� ���������: �������, �������.
                // ����� �� ���������� ���������� ������ ����� �������,
                // �������������� ������������ ����������� ���������.
                center: [55.76, 37.64],
                // ������� ���������������. ���������� ��������:
                // �� 0 (���� ���) �� 19.
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
                                // ���������� ������ ������ �����
                                myCoords, {
                                flying: true
                            }
                            )
                        }
                        // ���� ��� � �������.
                        else {
                            myPlacemark = new createPlacemark(myCoords);
                            myMap.geoObjects.add(myPlacemark);
                            // ������� ������� ��������� �������������� �� �����.
                            myPlacemark.events.add('dragend', function () {
                                getAddress(myPlacemark.geometry.getCoordinates());
                            });
                            myMap.panTo(
                                // ���������� ������ ������ �����
                                myCoords, {
                                flying: true
                            }
                            )
                        }
                        getAddress(myCoords);
                    });
                });
            }

            // ������� ���� �� �����.
            myMap.events.add('click', function (e) {
                //$('#id_objectname').empty();
                var coords = e.get('coords');

                // ���� ����� ��� ������� � ������ ����������� ��.
                if (myPlacemark) {
                    //$('#id_objectname').empty();
                    myPlacemark.geometry.setCoordinates(coords);
                }
                // ���� ��� � �������.
                else {
                    myPlacemark = createPlacemark(coords);
                    myMap.geoObjects.add(myPlacemark);
                    // ������� ������� ��������� �������������� �� �����.
                    myPlacemark.events.add('dragend', function () {
                        getAddress(myPlacemark.geometry.getCoordinates());
                    });
                }
                getAddress(coords);
            });

            // �������� �����.
            function createPlacemark(coords) {
                return new ymaps.Placemark(coords, {
                    iconCaption: '�����...'
                }, {
                    preset: 'islands#violetDotIconWithCaption',
                    draggable: true
                });
            }

            // ���������� ����� �� ����������� (�������� ��������������).
            function getAddress(coords) {
                //$('#id_objectname').empty();
                myPlacemark.properties.set('iconCaption', '�����...');
                ymaps.geocode(coords).then(function (res) {
                    var firstGeoObject = res.geoObjects.get(0);

                    myPlacemark.properties
                        .set({
                            // ��������� ������ � ������� �� �������.
                            iconCaption: [
                                // �������� ����������� ������ ��� ����������� ���������������-��������������� �����������.
                                firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                                // �������� ���� �� ��������, ���� ����� ������ null, ����������� ������������ ������.
                                firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                            ].filter(Boolean).join(', '),
                            // � �������� �������� ������ ������ ������ � ������� �������.
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
