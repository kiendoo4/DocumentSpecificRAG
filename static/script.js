const messageBar = document.querySelector(".bar-wrapper input");
const sendBtn = document.querySelector(".bar-wrapper button");
const messageBox = document.querySelector(".message-box");

sendBtn.onclick = function () {
  if(messageBar.value.length > 0){
    const UserTypedMessage = messageBar.value;
    messageBar.value = "";

    let message =
    `<div class="chat message">
    <img src="${userImgUrl}">
    <span>
      ${UserTypedMessage}
    </span>
  </div>`;

  let response =
  `<div class="chat response">
  <img src="${botImgUrl}">
  <span class= "new">...
  </span>
</div>`

    messageBox.insertAdjacentHTML("beforeend", message);
    messageBox.insertAdjacentHTML("beforeend", response);

    const requestOptions = {
      method : "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "message": UserTypedMessage
      })
    }

    fetch('/chat', requestOptions).then(res => res.json()).then(data => {
      const ChatBotResponse = document.querySelector(".response .new");
      ChatBotResponse.innerHTML = data.response;
      ChatBotResponse.classList.remove("new");
    }).catch((error) => {
      const ChatBotResponse = document.querySelector(".response .new");
      ChatBotResponse.innerHTML = "Oops! An error occurred. Please try again";
    })
  }
}
