const copyBtn = document.querySelector('.copy_btn');
const kakaoShare = document.querySelector('.kak_share');

$(function() {
    let url = location.href;
    let img = $('.result_img img').attr('src');
    $("meta[property='og\\:url']").attr('content', url);
    $("meta[property='og\\:image']").attr('content', img);
    const nickname = sessionStorage.getItem("nickname");
    const txt = document.getElementById("nickname");
    txt.innerHTML = nickname;
});

function copyUrl() {
    const url = window.location.href;

     navigator.clipboard.writeText(url).then(() => {
         alert("URL이 복사되었습니다"); 
     });
}


Kakao.init('c963b5273576eb43b2c68c2088700c47');

function sendLink() {
     let result_url = window.location.href;
     Kakao.Link.sendDefault({
         objectType: 'feed',
         content: {
             title: '어쩌다 국내여행',
             description: '나의 여행 성향은?',
             imageUrl:
                 'http://domestic-trip.com',
             link: {
                 mobileWebUrl: 'http://domestic-trip.com',
                 webUrl: 'http://domestic-trip.com',
             },
         },
         social: {
             likeCount: 286,
             commentCount: 45,
             sharedCount: 845,
         },
         buttons: [
         {
             title: '결과 보러가기',
             link: {
                 webUrl: result_url,
                 mobileWebUrl: result_url,
             },
         },
         {
             title: '테스트 하러가기',
             link: {
                 webUrl: 'http://domestic-trip.com',
                 mobileWebUrl: 'http://domestic-trip.com',
             },
         },
         ],
     });
 }

document.addEventListener('DOMContentLoaded', function () {
    const twitterShare = document.querySelector('.twi_btn');
    function shareTwitter() {
        var sendText = "나의 여행 성향은?!"; // 전달할 텍스트
        var sendUrl = "http://www.domestic-trip.com"; // 전달할 URL
        window.open("https://twitter.com/intent/tweet?text=" + encodeURIComponent(sendText) + "&url=" + encodeURIComponent(sendUrl));
    }
    twitterShare.addEventListener('click', shareTwitter);
});

copyBtn.addEventListener('click', copyUrl);
kakaoShare.addEventListener('click', sendLink);


function toggleCheckbox(checkboxId) {
    let checkbox = document.getElementById(checkboxId);
    checkbox.checked = !checkbox.checked;
}

let currentSlide = 0;
let slideCount = document.getElementsByClassName('spot-slide').length;

function showSlide(direction) {
    let slides = document.getElementsByClassName('spot-slide');
    slides[currentSlide].style.display = 'none';
    
    if (direction === 'prev') {
        currentSlide = (currentSlide - 1 + slideCount) % slideCount;
    } else if (direction === 'next') {
        currentSlide = (currentSlide + 1) % slideCount;
    }
    
    slides[currentSlide].style.display = 'block';
}


function validateSelection() {
        let checkboxes = document.getElementsByName('selected_spot');
        let selectedCount = 0;
        
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                selectedCount++;
            }
        }
        
        if (selectedCount <= 2) {
            alert('3곳 이상의 여행지를 선택해주세요.');
            return false; 
        }
        
        return true;
    }