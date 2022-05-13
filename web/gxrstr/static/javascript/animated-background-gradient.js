$('div[id^="animated-background-gradient"]').each(function (_) { // skipcq: JS-0069
    let thisID = $(this).attr("id");
    let color1 = $(`#${thisID}`).attr("data-color1");
    let color2 = $(`#${thisID}`).attr("data-color2");
    let color3 = $(`#${thisID}`).attr("data-color3");
    let color4 = $(`#${thisID}`).attr("data-color4");
    $("head").append(`<style type="text/css">body{background: linear-gradient(-45deg, ${color4}, ${color3}, ${color2}, ${color1});}</style>`);
    $("head").append('<style type="text/css">.animated-bg{background: rgba(255, 255, 255, 0.0)!important;}</style>');
});