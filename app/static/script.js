//Send message when button is clicked
document.getElementById("send-btn").addEventListener("click", sendMessage); 
// Send message when Enter key is pressed
document.getElementById("user-input").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

// Sends message to server and handles response
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    appendMessage("you", "You: " + message);
    input.value = "";

    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    })
    .then((res) => res.json())
    .then((data) => appendMessage("bot", "Bot: " + data.response))
    .catch(() => appendMessage("bot", "Bot: Sorry, there was a problem."));
}

// Function to add a message to the chat box
function appendMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = "message " + sender;
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}