import React from 'react';
import { Calendar, ArrowRight, Zap } from 'lucide-react';

const CTA = () => {
  return (
    <section id="cta" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-gray-800 via-black to-gray-900">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_25%,rgba(255,69,0,0.15),transparent_60%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <div className="inline-flex items-center space-x-2 px-6 py-3 bg-orange-500/20 rounded-full border border-orange-500/30 mb-8">
            <Zap className="w-5 h-5 text-orange-500" />
            <span className="text-orange-500 font-semibold">Limited Time Offer</span>
          </div>

          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6 leading-tight">
            Ready to <span className="text-orange-500">Transform</span> Your Business?
          </h2>
          
          <p className="text-xl text-gray-400 max-w-3xl mx-auto mb-12 leading-relaxed">
            Stop watching competitors pull ahead. Book a free consultation and discover 
            exactly how Chispa can automate your processes, optimize your marketing, 
            and accelerate your growth in the next 90 days.
          </p>

          <div className="space-y-8">
            {/* Main CTA Button */}
            <div className="inline-block">
              <button className="group relative px-12 py-6 bg-gradient-to-r from-orange-600 to-orange-500 rounded-2xl text-white font-bold text-xl hover:from-orange-500 hover:to-orange-400 transform hover:scale-105 transition-all duration-300 shadow-2xl hover:shadow-orange-500/30">
                <span className="flex items-center space-x-3">
                  <Calendar className="w-6 h-6" />
                  <span>Book Free Consultation</span>
                  <ArrowRight className="w-6 h-6 group-hover:translate-x-1 transition-transform" />
                </span>
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-r from-orange-600 to-orange-500 blur-xl opacity-30 group-hover:opacity-50 transition-opacity -z-10"></div>
              </button>
            </div>

            {/* Alternative CTA */}
            <div>
              <button className="group px-8 py-4 bg-transparent border-2 border-orange-500 rounded-xl text-orange-500 font-semibold text-lg hover:bg-orange-500 hover:text-white transition-all duration-300">
                <span className="flex items-center space-x-2">
                  <span>Let's Build Smarter</span>
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </span>
              </button>
            </div>
          </div>

          {/* Trust Indicators */}
          <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-6 bg-gray-800/30 rounded-xl backdrop-blur-sm">
              <div className="text-2xl font-bold text-orange-500 mb-2">100% Free</div>
              <p className="text-gray-400">No hidden fees or obligations</p>
            </div>
            <div className="text-center p-6 bg-gray-800/30 rounded-xl backdrop-blur-sm">
              <div className="text-2xl font-bold text-orange-500 mb-2">30 Minutes</div>
              <p className="text-gray-400">Quick strategy session</p>
            </div>
            <div className="text-center p-6 bg-gray-800/30 rounded-xl backdrop-blur-sm">
              <div className="text-2xl font-bold text-orange-500 mb-2">Custom Plan</div>
              <p className="text-gray-400">Tailored to your needs</p>
            </div>
          </div>

          {/* Chatbot Notice */}
          <div className="mt-12 p-6 bg-gradient-to-r from-orange-900/20 to-gray-900/30 rounded-xl border border-orange-500/30">
            <p className="text-orange-400 text-sm font-semibold">💬 AI Assistant Available</p>
            <p className="text-gray-300 text-xs mt-1">Chat with our AI assistant for instant answers about our services</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CTA;