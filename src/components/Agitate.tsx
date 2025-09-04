import React from 'react';
import { DollarSign, Target, Clock, Zap } from 'lucide-react';

const Agitate = () => {
  const consequences = [
    {
      icon: DollarSign,
      stat: "$50,000+",
      title: "Lost Revenue Annually",
      description: "From inefficient processes and missed opportunities while competitors capture your market share.",
    },
    {
      icon: Clock,
      stat: "40+ Hours",
      title: "Wasted Weekly",
      description: "Your team drowning in manual tasks instead of focusing on growth and innovation.",
    },
    {
      icon: Target,
      stat: "73%",
      title: "Marketing Budget Wasted",
      description: "On campaigns without proper targeting, tracking, or optimization strategies.",
    },
    {
      icon: Zap,
      stat: "6 Months",
      title: "Behind Competitors",
      description: "Who are already using AI and automation to scale faster and serve customers better.",
    },
  ];

  return (
    <section id="agitate" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-gray-800 via-gray-900 to-black">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_75%_75%,rgba(255,69,0,0.08),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            The Cost of <span className="text-red-500">Doing Nothing</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-4xl mx-auto leading-relaxed">
            While you hesitate, your competitors are already implementing the solutions that will dominate your market. 
            Here's exactly what staying behind is costing you right now.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
          {consequences.map((item, index) => {
            const Icon = item.icon;
            return (
              <div
                key={index}
                className="group text-center p-8 bg-gradient-to-b from-red-900/20 to-gray-900/50 rounded-2xl backdrop-blur-sm border border-red-700/30 hover:border-red-500/50 transition-all duration-500 hover:scale-105 hover:bg-gradient-to-b hover:from-red-900/30 hover:to-gray-900/50"
              >
                <div className="w-20 h-20 bg-red-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:bg-red-500/30 transition-colors duration-300">
                  <Icon className="w-10 h-10 text-red-500" />
                </div>
                
                <div className="text-3xl md:text-4xl font-bold text-red-500 mb-2 group-hover:text-red-400 transition-colors">
                  {item.stat}
                </div>
                
                <h3 className="text-xl font-bold text-white mb-4 group-hover:text-red-100 transition-colors">
                  {item.title}
                </h3>
                
                <p className="text-gray-400 text-sm leading-relaxed group-hover:text-gray-300 transition-colors">
                  {item.description}
                </p>
              </div>
            );
          })}
        </div>

        {/* Urgent Message */}
        <div className="text-center p-8 bg-gradient-to-r from-red-900/30 to-orange-900/30 rounded-2xl border border-red-500/30 backdrop-blur-sm">
          <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">
            Every Day You Wait, the Gap <span className="text-red-500">Widens</span>
          </h3>
          <p className="text-lg text-gray-300 max-w-3xl mx-auto">
            Your competitors aren't standing still. They're implementing AI, optimizing their operations, 
            and capturing the market share you could be claiming. The question isn't whether you can afford to modernize—
            it's whether you can afford not to.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Agitate;