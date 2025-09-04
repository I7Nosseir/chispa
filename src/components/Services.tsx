import React from 'react';
import { Bot, TrendingUp, Users, Globe, Palette, ArrowRight } from 'lucide-react';

const Services = () => {
  const services = [
    {
      icon: Bot,
      title: "AI Automation",
      subtitle: "Intelligent Workflows That Scale",
      description: "Transform your business operations with custom AI solutions that handle repetitive tasks, analyze data, and make intelligent decisions 24/7.",
      features: [
        "Custom chatbots and virtual assistants",
        "Automated data processing and analysis",
        "Intelligent workflow optimization",
        "API integrations and system automation"
      ],
      color: "from-blue-500/20 to-purple-500/20",
      hoverColor: "hover:from-blue-500/30 hover:to-purple-500/30"
    },
    {
      icon: TrendingUp,
      title: "Smart Marketing",
      subtitle: "Data-Driven Growth Strategies",
      description: "Stop guessing and start growing with marketing campaigns built on data, optimized for results, and transparent in their ROI.",
      features: [
        "Paid advertising (Google, Facebook, LinkedIn)",
        "SEO and content marketing",
        "Marketing automation and funnels",
        "Analytics and performance tracking"
      ],
      color: "from-green-500/20 to-teal-500/20",
      hoverColor: "hover:from-green-500/30 hover:to-teal-500/30"
    },
    {
      icon: Users,
      title: "Business Consultation",
      subtitle: "Strategic Technology Planning",
      description: "Get expert guidance on how technology can solve your business challenges and accelerate growth through strategic planning.",
      features: [
        "Technology strategy and roadmap",
        "Process optimization consulting",
        "Digital transformation planning",
        "Competitive analysis and positioning"
      ],
      color: "from-orange-500/20 to-red-500/20",
      hoverColor: "hover:from-orange-500/30 hover:to-red-500/30"
    },
    {
      icon: Globe,
      title: "Website Building & Improvement",
      subtitle: "Modern Web Experiences",
      description: "Fast, beautiful, conversion-focused websites that represent your brand professionally and turn visitors into customers.",
      features: [
        "Custom responsive website design",
        "E-commerce solutions",
        "Performance optimization",
        "SEO and conversion optimization"
      ],
      color: "from-purple-500/20 to-pink-500/20",
      hoverColor: "hover:from-purple-500/30 hover:to-pink-500/30"
    },
    {
      icon: Palette,
      title: "Design & Branding",
      subtitle: "Visual Identity That Converts",
      description: "Professional visual identity and design systems that build trust, communicate value, and differentiate you from competitors.",
      features: [
        "Logo and brand identity design",
        "Marketing materials and collateral",
        "UI/UX design for digital products",
        "Brand guidelines and style systems"
      ],
      color: "from-pink-500/20 to-rose-500/20",
      hoverColor: "hover:from-pink-500/30 hover:to-rose-500/30"
    }
  ];

  return (
    <section id="services" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-gray-800 via-black to-gray-900">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_75%_25%,rgba(255,69,0,0.1),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Our <span className="text-orange-500">Services</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-4xl mx-auto leading-relaxed">
            Comprehensive solutions designed to work together, creating a technology ecosystem 
            that grows with your business and delivers measurable results.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {services.map((service, index) => {
            const Icon = service.icon;
            return (
              <div
                key={index}
                className={`group relative p-8 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-2xl backdrop-blur-sm border border-gray-700/50 hover:border-orange-500/50 transition-all duration-500 hover:scale-[1.02] ${service.hoverColor}`}
              >
                <div className={`absolute inset-0 rounded-2xl bg-gradient-to-br ${service.color} opacity-0 group-hover:opacity-100 transition-opacity duration-500`}></div>
                
                <div className="relative z-10">
                  <div className="flex items-start justify-between mb-6">
                    <div className="w-16 h-16 bg-orange-500/20 rounded-2xl flex items-center justify-center group-hover:bg-orange-500/30 transition-colors duration-300">
                      <Icon className="w-8 h-8 text-orange-500" />
                    </div>
                    
                    <button className="opacity-0 group-hover:opacity-100 transition-opacity duration-300 p-2 bg-orange-500/20 rounded-full hover:bg-orange-500/30">
                      <ArrowRight className="w-5 h-5 text-orange-500" />
                    </button>
                  </div>
                  
                  <div className="mb-6">
                    <h3 className="text-2xl font-bold text-white mb-2 group-hover:text-orange-100 transition-colors">
                      {service.title}
                    </h3>
                    <p className="text-orange-500 font-semibold mb-4">
                      {service.subtitle}
                    </p>
                    <p className="text-gray-400 leading-relaxed group-hover:text-gray-300 transition-colors">
                      {service.description}
                    </p>
                  </div>

                  <div className="space-y-3">
                    <h4 className="text-white font-semibold">What's Included:</h4>
                    <ul className="space-y-2">
                      {service.features.map((feature, idx) => (
                        <li key={idx} className="flex items-start text-sm text-gray-400 group-hover:text-gray-300 transition-colors">
                          <div className="w-1.5 h-1.5 bg-orange-500 rounded-full mt-2 mr-3 flex-shrink-0"></div>
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <div className="absolute -inset-0.5 rounded-2xl bg-gradient-to-br from-orange-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10"></div>
              </div>
            );
          })}
        </div>

        {/* Integration Message */}
        <div className="mt-16 text-center p-8 bg-gradient-to-r from-orange-900/30 to-gray-900/50 rounded-2xl border border-orange-500/30 backdrop-blur-sm">
          <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">
            Better Together
          </h3>
          <p className="text-lg text-gray-300 max-w-4xl mx-auto leading-relaxed">
            These services aren't just individual offerings—they're designed to work together. 
            Your AI automation can feed data to your marketing campaigns, your new website can 
            showcase your refreshed branding, and our business consultation ties it all together 
            with a strategic roadmap for growth.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Services;