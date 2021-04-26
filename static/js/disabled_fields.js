 //////////////////////////////////////////////////////////////
        // для пунктов, где выбор активирует поля

        
        $("#id_techobespech_spravochnik_drugoe").prop("disabled", true);

        var select2 = document.querySelector('#id_techobespech_spravochnik_19');
        select2.addEventListener('change', () => {           
              $("#id_techobespech_spravochnik_drugoe").prop("disabled", false);                                
        });
        $("#id_techobespech_spravochnik_drugoe").prop("disabled", true);

        $("#id_videlenie_etapov").prop("disabled", true);
        var select1 = document.querySelector('#id_etapistroitelsta');
        select1.addEventListener('change', () => {
            if (select1.value == "Выделить этапы") {
                $("#id_videlenie_etapov").prop("disabled", false);
            }
            else {
                $("#id_videlenie_etapov").prop("disabled", true);
            }
        });

        $("#id_klassopasnosti_klass").prop("disabled", true);
        $("#id_klassopasnosti_category").prop("disabled", true);
        $("#id_opasniobekt").prop("disabled", true);
        var select = document.querySelector('#id_klassopasnosti');
        select.addEventListener('change', () => {
            if (select.value == "Принадлежит") {
                $("#id_klassopasnosti_klass").prop("disabled", false);
                $("#id_klassopasnosti_category").prop("disabled", false);
                $("#id_opasniobekt").prop("disabled", false);          
            }
            else {
                $("#id_klassopasnosti_klass").prop("disabled", true);
                $("#id_klassopasnosti_category").prop("disabled", true);
                $("#id_opasniobekt").prop("disabled", true);

            }
        });
        //////////////////////////////////////////////////////////////////