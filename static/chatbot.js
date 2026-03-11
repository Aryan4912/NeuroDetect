console.log("✅ chatbot.js loaded");

document.addEventListener("DOMContentLoaded", function () {

  // Toggle chatbot visibility
  window.toggleChatbot = function () {
    const bot = document.getElementById("chatbot-container");
    bot.style.display = bot.style.display === "none" ? "block" : "none";
  };

  // Handle user pressing Enter in input field
  window.handleChat = function (event) {
    if (event.key === "Enter") {
      const input = document.getElementById("chat-input");
      const userMessage = input.value.trim();
      if (userMessage === "") return;

      displayMessage("user", userMessage);   // Show user's message
      getBotResponse(userMessage);           // Get bot's reply

      input.value = "";
    }
  };

  // Display a message in the chat window
  function displayMessage(sender, message) {
    const chatBody = document.getElementById("chat-body");
    const msgDiv = document.createElement("div");
    msgDiv.style.margin = "5px 0";
    msgDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'NeuroBot'}:</strong> ${message}`;
    chatBody.appendChild(msgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  // Bot logic based on user message
  function getBotResponse(msg) {
  msg = msg.toLowerCase();
  let response = "I'm sorry, I didn’t understand that.";

  // 🔹 Specific intent: Medical advice
  if (msg.includes("what should i do") && msg.includes("brain tumor")) {
    response = "If you've been diagnosed with a brain tumor, consult a neurologist or neurosurgeon immediately. This website is not a substitute for professional medical advice.";
  } else if (msg.includes("when to consult") || msg.includes("realise") && msg.includes("doctor")) {
    response = "If you experience persistent headaches, vision issues, seizures, or personality changes, consult a neurologist right away.";
  } else if (msg.includes("is brain tumor rare")) {
    response = "Brain tumors are not extremely common, but they are not rare either. Early detection can make a big difference.";
  } else if (msg.includes("curable")) {
    response = "Some brain tumors are curable, especially if detected early and treated appropriately. Treatment success depends on the type and stage.";
  } else if (msg.includes("how much time") || msg.includes("expand") || msg.includes("serious")) {
    response = "Tumor growth rates vary. Some grow slowly over years, while others are aggressive. Only a scan and doctor can determine this accurately.";
  } else if (msg.includes("surgery") && msg.includes("advisable")) {
    response = "Surgery may be advisable depending on the tumor’s type, size, and location. Only your neurosurgeon can decide the best course.";
  } else if (msg.includes("success rate")) {
    response = "Success rates vary by tumor type and treatment approach. For some benign tumors, surgery is 90%+ successful. Malignant tumors may require additional therapy.";
  } else if (msg.includes("trust") && msg.includes("results")) {
    response = "Our AI tool provides high-accuracy predictions but should not replace professional diagnosis. Always consult a qualified doctor.";

  // 🔹 General questions about website
  } else if (msg.includes("what does this website do")) {
    response = "This website uses AI to detect and classify brain tumors from CT scans and provides a preliminary diagnostic report.";
  } else if (msg.includes("functionality") || msg.includes("features")) {
    response = "You can upload CT scans, get instant tumor predictions, view classifications, and download a diagnostic report.";

  // 🔹 Existing logic preserved
  } else if (msg.includes("upload") || msg.includes("ct scan")) {
    response = "Click on 'Upload CT Scan' to select your scan and get instant detection results.";
  } else if (msg.includes("types") || msg.includes("type of tumor")) {
    response = "We detect Glioma, Meningioma, and Pituitary tumors using AI.";
  } else if (msg.includes("accuracy")) {
    response = "Our model achieves accuracy of over 99.39%, but it should always be validated by a medical professional.";
  } else if (msg.includes("report") || msg.includes("download")) {
    response = "Once scanned, you can download an AI-generated diagnostic report in PDF format.";
  } else if (msg.includes("how to use") || msg.includes("guide")) {
    response = "Just upload your CT scan, and the system will detect and classify the tumor automatically.";
  } else if (
    msg.includes("what do you do") ||
    msg.includes("how does your ml model work") ||
    msg.includes("how your model works") ||
    msg.includes("what does your model do")
  ) {
    response = "We use a deep learning model trained on brain CT scans to detect and classify tumors. The image is processed, passed through a CNN (like ResNet or EfficientNet), and the tumor type is predicted along with an optional AI-generated report.";
  }

  setTimeout(() => displayMessage("bot", response), 500);
}
});
