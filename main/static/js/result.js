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


Kakao.init('0eca249734a4c539f4a34013bdea6ce0');

function sendLink() {
     let result_url = window.location.href;
     Kakao.Link.sendDefault({
         objectType: 'feed',
         content: {
             title: '어쩌다 국내여행',
             description: '나의 여행 성향은?',
             imageUrl:
                 'https://domestic-trip-sejxu.run.goorm.site',
             link: {
                 mobileWebUrl: 'https://domestic-trip-sejxu.run.goorm.site',
                 webUrl: 'https://domestic-trip-sejxu.run.goorm.site',
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
                 webUrl: 'https://domestic-trip-sejxu.run.goorm.site',
                 mobileWebUrl: 'https://domestic-trip-sejxu.run.goorm.site',
             },
         },
         ],
     });
 }


var instaShare = document.getElementById('insta_share');
instaShare.addEventListener('click', function() {
    var url = 'https://domestic-trip-sejxu.run.goorm.site'; // 공유할 URL
    var instagramShareUrl = 'https://www.instagram.com/share?url=' + encodeURIComponent(url);
    window.open(instagramShareUrl, '_blank');
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