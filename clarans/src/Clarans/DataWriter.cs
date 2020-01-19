using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

namespace Clarans
{
    public class DataWriter
    {
        public void WriteResult(string dataset, List<List<List<double>>> clusters, List<List<double>> medoids, double seconds)
        {
            var data = new
            {
                name = "KUB0462 - CLARANS",
                clusters,
                medoids,
                seconds
            };

            var json = JsonConvert.SerializeObject(data);

            File.WriteAllText($"../../results/{dataset}/clarans-csharp-results.json", json);
        }
    }
}