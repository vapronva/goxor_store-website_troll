$('div[id^="animated-background-gradient"]').each(function () {
    const thisID = $(this).attr("id"); // skipcq: JS-0069
    const color1 = $(`#${thisID}`).attr("data-color1");
    const color2 = $(`#${thisID}`).attr("data-color2");
    const color3 = $(`#${thisID}`).attr("data-color3");
    const color4 = $(`#${thisID}`).attr("data-color4");
    $("head").append(`<style type="text/css">body{background: linear-gradient(-45deg, ${color4}, ${color3}, ${color2}, ${color1});}</style>`);
    $("head").append('<style type="text/css">.animated-bg{background: rgba(255, 255, 255, 0.0)!important;}</style>');
});