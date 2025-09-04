import React from 'react';
import { ArrowRight, Zap, Cpu, Rocket } from 'lucide-react';

const Hero = () => {
  const scrollToNext = () => {
    const element = document.querySelector('#problem');
    element?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section id="home" className="min-h-screen flex items-center justify-center relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-black via-gray-900 to-black">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,69,0,0.1),transparent_50%)]"></div>
        <div className="absolute top-20 left-20 w-72 h-72 bg-orange-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-20 right-20 w-96 h-96 bg-orange-600/5 rounded-full blur-3xl animate-pulse delay-1000"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div className="space-y-8">
          {/* Floating Icons */}
          <div className="flex justify-center space-x-8 mb-8">
            <div className="p-4 bg-gray-800/50 rounded-2xl backdrop-blur-sm hover:bg-orange-500/20 hover:scale-110 transition-all duration-500 cursor-pointer group">
              <Zap className="w-8 h-8 text-orange-500 group-hover:text-orange-400" />
            </div>
            <div className="p-4 bg-gray-800/50 rounded-2xl backdrop-blur-sm hover:bg-orange-500/20 hover:scale-110 transition-all duration-500 cursor-pointer group delay-100">
              <Cpu className="w-8 h-8 text-orange-500 group-hover:text-orange-400" />
            </div>
            <div className="p-4 bg-gray-800/50 rounded-2xl backdrop-blur-sm hover:bg-orange-500/20 hover:scale-110 transition-all duration-500 cursor-pointer group delay-200">
              <Rocket className="w-8 h-8 text-orange-500 group-hover:text-orange-400" />
            </div>
          </div>

          {/* Main Headline */}
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-bold leading-tight">
            <span className="text-white">Custom Tech,</span>
            <br />
            <span className="text-orange-500 animate-pulse">Zero Fluff</span>
            <br />
            <span className="text-gray-300 text-3xl md:text-4xl lg:text-5xl font-light">
              Smart Solutions for Growth
            </span>
          </h1>

          <p className="text-xl md:text-2xl text-gray-400 max-w-3xl mx-auto leading-relaxed">
            Transform your business with AI automation, smart marketing strategies, 
            and cutting-edge web solutions that actually deliver results.
          </p>

          {/* CTA Button */}
          <div className="pt-8">
            <button 
              onClick={scrollToNext}
              className="group relative px-8 py-4 bg-gradient-to-r from-orange-600 to-orange-500 rounded-xl text-white font-semibold text-lg hover:from-orange-500 hover:to-orange-400 transform hover:scale-105 transition-all duration-300 shadow-2xl hover:shadow-orange-500/25"
            >
              <span className="flex items-center space-x-2">
                <span>Discover How</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </span>
              <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-orange-600 to-orange-500 blur opacity-30 group-hover:opacity-50 transition-opacity"></div>
            </button>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 border-2 border-orange-500 rounded-full flex justify-center">
          <div className="w-1 h-3 bg-orange-500 rounded-full mt-2 animate-pulse"></div>
        </div>
      </div>
    </section>
  );
};

export default Hero;