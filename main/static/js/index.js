document.addEventListener("DOMContentLoaded", function() {
    const nicknameInput = document.getElementById("nickname-input");
    const startButton = document.getElementById("start-button");

    nicknameInput.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            startButton.click();
        }
    });

    startButton.addEventListener("click", function(event) {
        if (nicknameInput.value.trim() === "") {
            event.preventDefault();
            alert("닉네임을 입력해주세요.");
        }
    });
});
