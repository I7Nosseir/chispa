import React from 'react';
import { Bot, TrendingUp, Users, Globe, Palette, CheckCircle } from 'lucide-react';

const Solution = () => {
  const solutions = [
    {
      icon: Bot,
      title: "AI Automation",
      description: "Transform repetitive tasks into intelligent workflows that run 24/7, freeing your team for strategic work.",
      benefits: ["Save 40+ hours weekly", "Reduce human error by 95%", "Scale without hiring"]
    },
    {
      icon: TrendingUp,
      title: "Smart Marketing",
      description: "Data-driven campaigns that actually convert, with transparent ROI tracking and continuous optimization.",
      benefits: ["3x better conversion rates", "50% lower acquisition costs", "Measurable results"]
    },
    {
      icon: Users,
      title: "Business Consultation",
      description: "Strategic guidance that aligns technology with your business goals for sustainable growth.",
      benefits: ["Clear growth roadmap", "Process optimization", "Competitive advantage"]
    },
    {
      icon: Globe,
      title: "Modern Websites",
      description: "Fast, beautiful, conversion-focused websites that turn visitors into customers.",
      benefits: ["Mobile-first design", "Lightning-fast loading", "SEO optimized"]
    },
    {
      icon: Palette,
      title: "Design & Branding",
      description: "Professional visual identity that builds trust and makes you stand out from competitors.",
      benefits: ["Professional credibility", "Brand consistency", "Customer trust"]
    }
  ];

  return (
    <section id="solution" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-black via-gray-900 to-gray-800">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,69,0,0.1),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Meet Your <span className="text-orange-500">Smart Solution</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-4xl mx-auto leading-relaxed">
            Chispa isn't just another agency. We're your strategic technology partner, 
            delivering custom solutions that eliminate inefficiencies and accelerate growth—without the fluff.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          {solutions.map((solution, index) => {
            const Icon = solution.icon;
            return (
              <div
                key={index}
                className="group relative p-8 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-2xl backdrop-blur-sm border border-gray-700/50 hover:border-orange-500/50 transition-all duration-500 hover:scale-105"
              >
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-orange-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                
                <div className="relative z-10">
                  <div className="w-16 h-16 bg-orange-500/20 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-orange-500/30 transition-colors duration-300">
                    <Icon className="w-8 h-8 text-orange-500" />
                  </div>
                  
                  <h3 className="text-2xl font-bold text-white mb-4 group-hover:text-orange-100 transition-colors">
                    {solution.title}
                  </h3>
                  
                  <p className="text-gray-400 mb-6 leading-relaxed group-hover:text-gray-300 transition-colors">
                    {solution.description}
                  </p>

                  <ul className="space-y-2">
                    {solution.benefits.map((benefit, idx) => (
                      <li key={idx} className="flex items-center text-sm text-gray-500 group-hover:text-gray-400 transition-colors">
                        <CheckCircle className="w-4 h-4 text-green-500 mr-2 flex-shrink-0" />
                        {benefit}
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="absolute -inset-0.5 rounded-2xl bg-gradient-to-br from-orange-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10"></div>
              </div>
            );
          })}
        </div>

        {/* Value Proposition */}
        <div className="text-center p-8 bg-gradient-to-r from-orange-900/30 to-gray-900/50 rounded-2xl border border-orange-500/30 backdrop-blur-sm">
          <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">
            Why Choose <span className="text-orange-500">Chispa?</span>
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-8">
            <div className="text-center">
              <div className="text-3xl font-bold text-orange-500 mb-2">Custom</div>
              <p className="text-gray-300">Tailored solutions, not one-size-fits-all templates</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-orange-500 mb-2">Results</div>
              <p className="text-gray-300">Measurable outcomes that impact your bottom line</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-orange-500 mb-2">Partnership</div>
              <p className="text-gray-300">Ongoing support, not just a one-time project</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Solution;