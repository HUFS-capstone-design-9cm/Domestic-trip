const copyBtn = document.querySelector('.copy_btn');
const kakaoShare = document.querySelector('.kak_share');

$(function() {
    let url = location.href;
    let img = $('.result_img img').attr('src');
    $("meta[property='og\\:url']").attr('content', url);
    $("meta[property='og\\:image']").attr('content', img);
});

// function copyUrl() {
//     let tmp = document.createElement('input');
//     let url = location.href;

//     document.body.appendChild(tmp);
//     tmp.value = url;
//     tmp.select();
//     document.execCommand("copy");
//     document.body.removeChild(tmp);

//     alert("URL이 복사되었습니다.");
// }

function copyUrl() {
    const url = window.location.href;

    navigator.clipboard.writeText(url).then(() => {
        alert("URL이 복사되었습니다"); 
    });
}

Kakao.init('0eca249734a4c539f4a34013bdea6ce0');
//Kakao.isInitialized();

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