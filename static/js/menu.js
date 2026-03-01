
$(document).ready(function(){

    /* =========================
       TOGGLE MENU PRINCIPAL
    ========================== */
    $("#dt-menu-toggle").on("click", function(){
        $("#menu-main-menu").slideToggle(300);
        $(this).toggleClass("active");
    });

    /* =========================
       TOGGLE SUBMENUS
    ========================== */
    $(".dt-menu-expand").on("click", function(e){
        e.preventDefault();
        e.stopPropagation();

        let parentLi = $(this).closest("li");
        let submenu = parentLi.children(".sub-menu");

        if(submenu.length){
            submenu.slideToggle(300);
            parentLi.toggleClass("open");
            $(this).text(parentLi.hasClass("open") ? "−" : "+");
        }
    });

    /* =========================
       CERRAR OTROS SUBMENUS (OPCIONAL)
    ========================== */
    $(".menu > li > a").on("click", function(){
        $(".menu li").removeClass("open");
        $(".sub-menu").slideUp(200);
        $(".dt-menu-expand").text("+");
    });

});

