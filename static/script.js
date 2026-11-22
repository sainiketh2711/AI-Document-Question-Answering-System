// ==============================
// ELEMENTS
// ==============================

const questionInput = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");
const messages = document.getElementById("messages");
const welcomeScreen = document.getElementById("welcomeScreen");
const chatContainer = document.getElementById("chatContainer");


// ==============================
// SEND QUESTION
// ==============================

async function sendQuestion(question = null) {

    const userQuestion = question || questionInput.value.trim();

    if (!userQuestion) {
        return;
    }

    // Hide welcome screen
    welcomeScreen.style.display = "none";

    // Display user's question
    addMessage(userQuestion, "user");

    // Clear input
    questionInput.value = "";
    questionInput.style.height = "auto";

    // Disable button while processing
    askButton.disabled = true;

    // Show loading animation
    const loadingMessage = showLoading();

    try {

        // Send question to Flask backend
        const response = await fetch("/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: userQuestion
            })
        });

        const data = await response.json();

        // Remove loading animation
        loadingMessage.remove();

        if (!response.ok) {

            addMessage(
                data.error || "Something went wrong.",
                "assistant"
            );

            return;
        }

        // Display AI answer
        addMessage(data.answer, "assistant");

    } catch (error) {

        loadingMessage.remove();

        addMessage(
            "Unable to connect to the server. Please make sure the website is running.",
            "assistant"
        );

        console.error("Error:", error);

    } finally {

        askButton.disabled = false;

        questionInput.focus();
    }

}


// ==============================
// DISPLAY MESSAGE
// ==============================

function addMessage(text, type) {

    const message = document.createElement("div");

    message.className = `message ${type}`;

    const avatar = document.createElement("div");

    avatar.className = "message-avatar";

    avatar.textContent = type === "user" ? "👤" : "📚";

    const content = document.createElement("div");

    content.className = "message-content";

    const label = document.createElement("div");

    label.className = "message-label";

    label.textContent = type === "user" ? "You" : "Library AI";

    const bubble = document.createElement("div");

    bubble.className = "message-bubble";

    // Safe text display
    bubble.textContent = text;

    content.appendChild(label);
    content.appendChild(bubble);

    message.appendChild(avatar);
    message.appendChild(content);

    messages.appendChild(message);

    scrollToBottom();

}


// ==============================
// LOADING ANIMATION
// ==============================

function showLoading() {

    const message = document.createElement("div");

    message.className = "message assistant";

    message.innerHTML = `
        <div class="message-avatar">📚</div>

        <div class="message-content">

            <div class="message-label">
                Library AI
            </div>

            <div class="message-bubble loading-bubble">

                <span></span>
                <span></span>
                <span></span>

            </div>

        </div>
    `;

    messages.appendChild(message);

    scrollToBottom();

    return message;

}


// ==============================
// EXAMPLE QUESTIONS
// ==============================

function askExample(button) {

    const question = button.textContent.trim();

    sendQuestion(question);

}


// ==============================
// NEW CONVERSATION
// ==============================

function clearChat() {

    messages.innerHTML = "";

    welcomeScreen.style.display = "block";

    questionInput.value = "";

    questionInput.style.height = "auto";

    questionInput.focus();

    scrollToBottom();

}


// ==============================
// AUTO SCROLL
// ==============================

function scrollToBottom() {

    chatContainer.scrollTop = chatContainer.scrollHeight;

}


// ==============================
// ENTER KEY
// ==============================

questionInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendQuestion();

    }

});


// ==============================
// AUTO RESIZE TEXTAREA
// ==============================

questionInput.addEventListener("input", function () {

    this.style.height = "auto";

    this.style.height = Math.min(
        this.scrollHeight,
        120
    ) + "px";

});