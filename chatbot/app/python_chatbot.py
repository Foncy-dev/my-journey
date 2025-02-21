import { useState } from "react";
import { Mic, MessageCircle, User, Plus } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import axios from "axios";

export default function Dashboard() {
  const [chatOpen, setChatOpen] = useState(false);
  const [userMessage, setUserMessage] = useState("");
  const [botReply, setBotReply] = useState("");

  const handleChat = async () => {
    if (!userMessage.trim()) return;

    try {
      const response = await axios.post("http://localhost:3001/api/chat", {
        message: userMessage,
      });
      setBotReply(response.data.botReply);
    } catch (error) {
      setBotReply("Error communicating with chatbot.");
      console.error("Chatbot API Error:", error);
    }
  };

  return (
    <div className="min-h-screen bg-black text-white p-4 flex flex-col gap-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-2">
          <User className="w-8 h-8 bg-gray-800 p-1 rounded-full" />
          <span className="text-lg">Hi, User 👋</span>
        </div>
        <Button className="bg-gray-700 px-4 py-2 rounded-lg flex items-center gap-2">
          <Plus className="w-5 h-5" /> Invite
        </Button>
      </div>

      {/* Chat Interface */}
      <div className="w-full flex flex-col items-center gap-2">
        <div className="w-32 h-32 bg-gray-900 rounded-full flex flex-col items-center justify-center shadow-lg">
          <span className="text-lg">Tap to Chat</span>
          <Mic className="w-6 h-6 mt-2" />
        </div>
        <input
          type="text"
          className="bg-gray-800 text-white p-2 rounded-md w-3/4"
          placeholder="Type your message..."
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
        />
        <Button onClick={handleChat} className="bg-blue-500 px-4 py-2 rounded-lg mt-2">Send</Button>
        {botReply && <div className="mt-4 p-2 bg-gray-700 rounded-lg w-3/4">{botReply}</div>}
      </div>

      {/* Explore Section */}
      <div>
        <h2 className="text-xl font-semibold">Explore</h2>
        <div className="grid grid-cols-2 gap-4 mt-4">
          <Card className="bg-gray-800 text-white p-4">
            <CardContent>
              <span className="block text-lg">🎨 Art</span>
              <p className="text-sm text-gray-400">Create digital art, from sketches to finished pieces.</p>
            </CardContent>
          </Card>
          <Card className="bg-gray-800 text-white p-4">
            <CardContent>
              <span className="block text-lg">🧳 Booking</span>
              <p className="text-sm text-gray-400">Find stays, flights, car rentals, and more.</p>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Bottom Navigation */}
      <div className="fixed bottom-4 left-1/2 transform -translate-x-1/2 flex gap-6 bg-gray-900 p-3 rounded-full">
        <MessageCircle className="w-6 h-6 text-white" />
        <Mic className="w-6 h-6 text-white" />
        <User className="w-6 h-6 text-white" />
      </div>
    </div>
  );
}
