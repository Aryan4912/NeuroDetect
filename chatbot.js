function toggleChatbot() {
    const bot = document.getElementById("chatbot-container");
    bot.style.display = bot.style.display === "none" ? "block" : "none";
  }
  
  function handleChat(event) {
    if (event.key === "Enter") {
      const input = document.getElementById("chat-input");
      const message = input.value.trim();
      if (message) {
        displayMessage("user", message);
        getBotResponse(message.toLowerCase());
        input.value = "";
      }
    }
  }
  
  function displayMessage(sender, message) {
    const chatBody = document.getElementById("chat-body");
    const msgDiv = document.createElement("div");
    msgDiv.style.margin = "5px 0";
    msgDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'NeuroBot'}:</strong> ${message}`;
    chatBody.appendChild(msgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
  }
  
  function getBotResponse(msg) {
    let response = "I'm sorry, I didn’t understand that.";
  
    if (msg.includes("upload") || msg.includes("ct scan")) {
      response = "Click on 'Upload CT Scan' to select your scan and get instant detection results.";
    } else if (msg.includes("types") || msg.includes("tumor")) {
      response = "We detect Glioma, Meningioma, and Pituitary tumors using AI.";
    } else if (msg.includes("accuracy")) {
      response = "Our model achieves accuracy of over 97%, but it should always be validated by a medical professional.";
    } else if (msg.includes("report")) {
      response = "Once scanned, you can download an AI-generated diagnostic report in PDF format.";
    } else if (msg.includes("how to use")) {
      response = "Just upload your CT scan, and the system will detect and classify the tumor automatically.";
    } else if (msg.includes("what do you do") || msg.includes("how does your ml model work") || msg.includes("how your model works") || msg.includes("what does your model do")) {
      response = "We use a deep learning model trained on brain CT scans to detect and classify tumors. The image is processed, passed through a CNN (like ResNet or EfficientNet), and the tumor type is predicted along with an optional AI-generated report.";
    }
  
    setTimeout(() => displayMessage("bot", response), 500);
  }
  