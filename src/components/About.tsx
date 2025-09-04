import React from 'react';
import { Target, Shield, Award, Users } from 'lucide-react';

const About = () => {
  const values = [
    {
      icon: Target,
      title: "Custom Tech, Zero Fluff",
      description: "We cut through the noise to deliver exactly what your business needs—no unnecessary complexity, just results."
    },
    {
      icon: Shield,
      title: "Trust & Transparency",
      description: "Clear communication, honest pricing, and measurable outcomes. You always know where your investment is going."
    },
    {
      icon: Award,
      title: "Proven Expertise",
      description: "Years of experience across AI, marketing, web development, and business strategy—all under one roof."
    },
    {
      icon: Users,
      title: "True Partnership",
      description: "We're not just vendors—we're strategic partners invested in your long-term success and growth."
    }
  ];

  return (
    <section id="about" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-gray-900 via-black to-gray-800">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_25%_75%,rgba(255,69,0,0.08),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            About <span className="text-orange-500">Chispa</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-4xl mx-auto leading-relaxed">
            We're not your typical agency. Chispa combines cutting-edge technology with proven business strategy 
            to deliver solutions that actually move the needle for your business.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 mb-16">
          {/* Mission Statement */}
          <div className="space-y-8">
            <div className="p-8 bg-gradient-to-br from-orange-900/20 to-gray-900/50 rounded-2xl border border-orange-500/30 backdrop-blur-sm">
              <h3 className="text-2xl font-bold text-white mb-4">Our Mission</h3>
              <p className="text-gray-300 leading-relaxed mb-6">
                To bridge the gap between cutting-edge technology and practical business results. 
                We believe every business deserves access to enterprise-level solutions without 
                the enterprise-level complexity or cost.
              </p>
              <div className="flex items-center space-x-2 text-orange-500">
                <Target className="w-5 h-5" />
                <span className="font-semibold">Custom Tech, Zero Fluff</span>
              </div>
            </div>

            <div className="p-8 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-2xl border border-gray-700/50 backdrop-blur-sm">
              <h3 className="text-2xl font-bold text-white mb-4">Why We're Different</h3>
              <ul className="space-y-3 text-gray-300">
                <li className="flex items-start space-x-2">
                  <div className="w-2 h-2 bg-orange-500 rounded-full mt-2 flex-shrink-0"></div>
                  <span>We speak business, not just tech</span>
                </li>
                <li className="flex items-start space-x-2">
                  <div className="w-2 h-2 bg-orange-500 rounded-full mt-2 flex-shrink-0"></div>
                  <span>Every solution is custom-built for your goals</span>
                </li>
                <li className="flex items-start space-x-2">
                  <div className="w-2 h-2 bg-orange-500 rounded-full mt-2 flex-shrink-0"></div>
                  <span>Transparent pricing and measurable results</span>
                </li>
                <li className="flex items-start space-x-2">
                  <div className="w-2 h-2 bg-orange-500 rounded-full mt-2 flex-shrink-0"></div>
                  <span>Ongoing partnership, not one-time projects</span>
                </li>
              </ul>
            </div>
          </div>

          {/* Values Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {values.map((value, index) => {
              const Icon = value.icon;
              return (
                <div
                  key={index}
                  className="group p-6 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-2xl backdrop-blur-sm border border-gray-700/50 hover:border-orange-500/50 transition-all duration-500 hover:scale-105"
                >
                  <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-orange-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                  
                  <div className="relative z-10">
                    <div className="w-12 h-12 bg-orange-500/20 rounded-xl flex items-center justify-center mb-4 group-hover:bg-orange-500/30 transition-colors duration-300">
                      <Icon className="w-6 h-6 text-orange-500" />
                    </div>
                    
                    <h3 className="text-lg font-bold text-white mb-3 group-hover:text-orange-100 transition-colors">
                      {value.title}
                    </h3>
                    
                    <p className="text-gray-400 text-sm leading-relaxed group-hover:text-gray-300 transition-colors">
                      {value.description}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Unique Value Section */}
        <div className="text-center p-8 bg-gradient-to-r from-gray-800/50 to-gray-900/50 rounded-2xl border border-gray-700/50 backdrop-blur-sm">
          <h3 className="text-2xl md:text-3xl font-bold text-white mb-6">
            The <span className="text-orange-500">Chispa</span> Difference
          </h3>
          <p className="text-lg text-gray-300 max-w-4xl mx-auto leading-relaxed">
            While others sell you what they have, we build what you need. Our unique blend of 
            AI automation, marketing expertise, web development, and business strategy creates 
            solutions that are greater than the sum of their parts—just like the spark that 
            ignites transformation.
          </p>
        </div>
      </div>
    </section>
  );
};

export default About;