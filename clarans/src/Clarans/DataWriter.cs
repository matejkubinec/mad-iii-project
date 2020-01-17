using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Clarans
{
    public class DataWriter
    {
        public void WriteResult(List<List<List<double>>> clusters, List<List<double>> medoids)
        {
            var data = new
            {
                clusters,
                medoids
            };

            var json = JsonConvert.SerializeObject(data);

            File.WriteAllText("clarans-csharp-results.json", json);
        }
    }
}