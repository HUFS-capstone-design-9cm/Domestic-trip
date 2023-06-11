function scrollUp(top) {
    const vheight = $('.test').height();
    const margin_top = parseInt($('#survey').css('margin-top'), 10);
    $('html, body').animate({
        scrollTop: top - vheight - margin_top
    }, 500);
}

function scrollDown(top) {
    const vheight = $('.test').height();
    const margin_top = parseInt($('#survey').css('margin-top'), 10);
    $('html, body').animate({
        scrollTop: vheight + top - margin_top
    }, 500);
}

$(function() {
    $('.scene_next_btn').click(function(e){
        let divs = $(this).parent().prev().children();
        let present_top = $(this).parent().parent()[0].offsetTop;
        e.preventDefault();
        scrollDown(present_top);
    });

    $('.scene_prev_btn').click(function(e){
        let present_top = $(this).parent().parent()[0].offsetTop;
        e.preventDefault();
        scrollUp(present_top);
    });
    
    $('.next_btn').click(function (e) {
        let divs = $(this).parent().prev().children();
        let present_top = $(this).parent().parent()[0].offsetTop;
        let inputs = divs.find('input:checked');
        if (inputs.length < 1) {
            alert('문항이 선택되지 않았습니다.');
            return false;
        }
        e.preventDefault();
        scrollDown(present_top);
    });

    $('.prev_btn').click(function (e) {
        let present_top = $(this).parent().parent()[0].offsetTop;
        e.preventDefault();
        scrollUp(present_top);
    });

    $('#form').submit(function(e) {
        let radios = $('input[type=radio]:checked').length;
        if (radios < 9) {
            alert('모든 문항에 답하지 않았습니다.');
            return false;
        }
        alert('결과 페이지로 이동합니다! 결과 페이지 하단에서 ‘경로 추천’을 받은 후 만족도 조사까지 제출 부탁드립니다. 피드백은 저희에게 큰 도움이 됩니다. :-)');
        return true;
    });

    $('html, body').animate({
        scrollTop: 0
    }, 500);
});
