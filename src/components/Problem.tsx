import React from 'react';
import { AlertTriangle, Clock, TrendingDown, Users } from 'lucide-react';

const Problem = () => {
  const problems = [
    {
      icon: Clock,
      title: "Manual Processes Killing Productivity",
      description: "Your team spends hours on repetitive tasks that could be automated, draining valuable time from strategic work.",
    },
    {
      icon: TrendingDown,
      title: "Marketing That Misses the Mark",
      description: "Throwing money at ads without data-driven strategy, watching budgets disappear with minimal returns.",
    },
    {
      icon: AlertTriangle,
      title: "Outdated Websites Losing Customers",
      description: "Your online presence looks like it's from 2010, driving potential clients straight to competitors.",
    },
    {
      icon: Users,
      title: "Inefficient Business Operations",
      description: "Disconnected systems and processes creating bottlenecks, confusion, and missed opportunities daily.",
    },
  ];

  return (
    <section id="problem" className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-black via-gray-900 to-gray-800">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_25%_25%,rgba(255,69,0,0.05),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Your Business Is <span className="text-orange-500">Bleeding Money</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Every day you delay modernizing your operations, you're losing revenue to smarter competitors who've embraced automation and digital excellence.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {problems.map((problem, index) => {
            const Icon = problem.icon;
            return (
              <div
                key={index}
                className="group relative p-8 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-2xl backdrop-blur-sm border border-gray-700/50 hover:border-orange-500/50 transition-all duration-500 hover:scale-105 hover:bg-gradient-to-br hover:from-orange-900/20 hover:to-gray-900/50"
              >
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-orange-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                
                <div className="relative z-10">
                  <div className="w-16 h-16 bg-orange-500/20 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-orange-500/30 transition-colors duration-300">
                    <Icon className="w-8 h-8 text-orange-500" />
                  </div>
                  
                  <h3 className="text-2xl font-bold text-white mb-4 group-hover:text-orange-100 transition-colors">
                    {problem.title}
                  </h3>
                  
                  <p className="text-gray-400 leading-relaxed group-hover:text-gray-300 transition-colors">
                    {problem.description}
                  </p>
                </div>

                <div className="absolute -inset-0.5 rounded-2xl bg-gradient-to-br from-orange-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10"></div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Problem;