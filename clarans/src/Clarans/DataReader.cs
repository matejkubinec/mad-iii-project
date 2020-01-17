using System.IO;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Clarans
{
    public class DataReader
    {
        public async Task<List<List<double>>> ReadFile(string filepath)
        {
            var lines = await File.ReadAllLinesAsync(filepath);
            var data = new List<List<double>>();

            foreach (var line in lines)
            {
                var values = new List<double>();

                foreach (var value in line.Split(" "))
                {
                    if (string.IsNullOrWhiteSpace(value))
                    {
                        continue;
                    }
                    else
                    {
                        values.Add(double.Parse(value));
                    }
                }

                data.Add(values);
            }

            return data;
        }
    }
}