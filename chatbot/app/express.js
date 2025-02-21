const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

const PYTHON_CHATBOT_URL = "http://127.0.0.1:5000/chat"; // Update with Flask API URL

// Route to handle chat messages
app.post("/api/chat", async (req, res) => {
    try {
        const userMessage = req.body.message;
        
        // Send user message to Python chatbot
        const response = await axios.post(PYTHON_CHATBOT_URL, { message: userMessage });
        
        res.json({ botReply: response.data.reply });
    } catch (error) {
        console.error("Error communicating with chatbot:", error);
        res.status(500).json({ error: "Failed to get response from chatbot." });
    }
});

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});