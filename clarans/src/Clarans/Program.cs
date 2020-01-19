using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;

namespace Clarans
{
    class Program
    {
        private static string RootDir
        {
            get
            {
                var location = Assembly.GetExecutingAssembly().Location;
                var path = Path.GetDirectoryName(location);
                return Path.Combine(path, "..", "..", "..");
            }
        }

        public static async Task Iris()
        {
            var path = Path.Combine(RootDir, "..", "..", "data", "iris.txt");
            var filename = Path.GetFullPath(path);
            var writer = new DataWriter();
            var reader = new DataReader();
            var clarans = new Clarans();

            var k = 3;
            var maxNeighbours = 3;
            var numLocal = 10;

            var data = await reader.ReadFile(filename);

            var stopwatch = new Stopwatch();
            stopwatch.Start();
            var result = clarans.Process(data, maxNeighbours, numLocal, k);
            stopwatch.Stop();

            var seconds = stopwatch.ElapsedMilliseconds / 1000.0;
            var clusters = new List<List<List<double>>>();
            var medoids = new List<List<double>>();

            foreach (var pair in result)
            {
                clusters.Add(pair.Value);
                medoids.Add(pair.Key);
            }

            writer.WriteResult("iris", clusters, medoids, seconds);
        }

        public static async Task Wine()
        {
            var path = Path.Combine(RootDir, "..", "..", "data", "wine.txt");
            var filename = Path.GetFullPath(path);
            var writer = new DataWriter();
            var reader = new DataReader();
            var clarans = new Clarans();

            var k = 2;
            var maxNeighbours = 4;
            var numLocal = 10;

            var data = await reader.ReadFile(filename);

            var stopwatch = new Stopwatch();
            stopwatch.Start();
            var result = clarans.Process(data, maxNeighbours, numLocal, k);
            stopwatch.Stop();

            var seconds = stopwatch.ElapsedMilliseconds / 1000.0;
            var clusters = new List<List<List<double>>>();
            var medoids = new List<List<double>>();

            foreach (var pair in result)
            {
                clusters.Add(pair.Value);
                medoids.Add(pair.Key);
            }

            writer.WriteResult("wine", clusters, medoids, seconds);
        }

        public static async Task Yeast()
        {
            var path = Path.Combine(RootDir, "..", "..", "data", "yeast.txt");
            var filename = Path.GetFullPath(path);
            var writer = new DataWriter();
            var reader = new DataReader();
            var clarans = new Clarans();

            var k = 10;
            var maxNeighbours = 5;
            var numLocal = 10;

            var data = await reader.ReadFile(filename);

            var stopwatch = new Stopwatch();
            stopwatch.Start();
            var result = clarans.Process(data, maxNeighbours, numLocal, k);
            stopwatch.Stop();

            var seconds = stopwatch.ElapsedMilliseconds / 1000.0;
            var clusters = new List<List<List<double>>>();
            var medoids = new List<List<double>>();

            foreach (var pair in result)
            {
                clusters.Add(pair.Value);
                medoids.Add(pair.Key);
            }

            writer.WriteResult("yeast", clusters, medoids, seconds);
        }

        static async Task Main(string[] args)
        {
            await Iris();
            await Wine();
            await Yeast();
        }
    }
}
