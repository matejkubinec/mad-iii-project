using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Clarans
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var datasets = new List<string>
            {
                "../../data/iris.txt",
                "../../data/wine.txt",
                "../../data/yeast.txt",
                "../../data/breast.txt",
            };
            var filename = datasets[0];
            var writer = new DataWriter();
            var reader = new DataReader();
            var clarans = new Clarans();

            var k = 5;
            var maxNeighbours = 5;
            var numLocal = 5;

            var data = await reader.ReadFile(filename);
            var result = clarans.Process(data, maxNeighbours, numLocal, k);

            var clusters = new List<List<List<double>>>();
            var medoids = new List<List<double>>();

            foreach (var pair in result)
            {
                clusters.Add(pair.Value);
                medoids.Add(pair.Key);
            }

            writer.WriteResult(clusters, medoids);
        }
    }
}
