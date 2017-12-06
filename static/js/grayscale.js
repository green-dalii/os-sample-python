// jQuery to collapse the navbar on scroll
function collapseNavbar() {
    if ($(".navbar").offset().top > 300) {
        $(".navbar-default").addClass("top-nav-collapse");
        $(".navbar-brand>img#logo1").css("display","none");
        $(".navbar-brand>img#logo2").css("display","block");
    } else {
        $(".navbar-default").removeClass("top-nav-collapse");
        $(".navbar-brand>img#logo1").css("display","block");
        $(".navbar-brand>img#logo2").css("display","none");
    }
}

$(window).scroll(collapseNavbar);
$(document).ready(collapseNavbar);