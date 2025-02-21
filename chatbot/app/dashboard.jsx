import { useState } from "react";
import { Mic, MessageCircle, User, Plus } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function Dashboard() {
  const [chatOpen, setChatOpen] = useState(false);

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

      {/* Chat Bubble */}
      <div
        className="w-full flex flex-col items-center gap-2 cursor-pointer"
        onClick={() => setChatOpen(true)}
      >
        <div className="w-32 h-32 bg-gray-900 rounded-full flex flex-col items-center justify-center shadow-lg">
          <span className="text-lg">Tap to Chat</span>
          <Mic className="w-6 h-6 mt-2" />
        </div>
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
