using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace Clarans.Test
{
    public class ClaransTests
    {
        [Fact]
        public void DistanceTest()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 1, 1, 1 };

            Assert.Equal(0, cl.Distance(v1, v2));

            v1 = new List<double> { 1, 1, 1 };
            v2 = new List<double> { 2, 2, 2 };

            Assert.Equal(Math.Sqrt(3), cl.Distance(v1, v2));
        }

        [Fact]
        public void FindNearestTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };
            var m = new List<List<double>> { v1, v3 };
            var n1 = cl.FindNearestMedoid(m, v2);
            var n2 = cl.FindNearestMedoid(m, v4);

            Assert.Equal(v1, n1);
            Assert.Equal(v3, n2);
        }

        [Fact]
        public void ClusterizeTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };

            var medoids = new List<List<double>> { v1, v3 };
            var vectors = new List<List<double>> { v1, v2, v3, v4 };
            var clusters = cl.Clusterize(medoids, vectors);

            Assert.Equal(2, clusters.Keys.Count);
            Assert.Equal(2, clusters[v1].Count);
            Assert.Equal(2, clusters[v3].Count);
        }

        [Fact]
        public void ChooseMedoidsTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v = new List<List<double>> { v1, v2 };
            var m = cl.ChooseMedoids(v, 2);
            Assert.Equal(v, m.OrderBy(v => v[0]).ToList());
        }

        [Fact]
        public void ComputeCostTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };

            var medoids = new List<List<double>> { v1, v3 };
            var vectors = new List<List<double>> { v1, v2, v3, v4 };
            var clusters = cl.Clusterize(medoids, vectors);
            var cost = cl.ComputeCost(clusters);

            Assert.Equal(2 * Math.Sqrt(3), cost);
        }

        [Fact]
        public void ProcessTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };
            var v = new List<List<double>> { v1, v2, v3, v4 };

            var clusters = cl.Process(v, 1, 100, 2);

            Assert.Equal(2, clusters.Count);

            var cl1 = clusters.Where(cl => cl.Key[0] == 1 || cl.Key[0] == 2).First();
            var cl2 = clusters.Where(cl => cl.Key[0] == 8 || cl.Key[0] == 9).First();

            Assert.Equal(2, cl1.Value.Count);
            Assert.Equal(2, cl2.Value.Count);

            var m1 = cl1.Key;
            var m2 = cl2.Key;

            Assert.InRange(m1[0], 1, 2);
            Assert.InRange(m2[0], 8, 9);

            var cl1_v1 = cl1.Value.FirstOrDefault(v => v[0] == 1);
            var cl1_v2 = cl1.Value.FirstOrDefault(v => v[0] == 2);

            Assert.NotNull(cl1_v1);
            Assert.NotNull(cl1_v2);

            var cl2_v1 = cl2.Value.FirstOrDefault(v => v[0] == 8);
            var cl2_v2 = cl2.Value.FirstOrDefault(v => v[0] == 9);

            Assert.NotNull(cl2_v1);
            Assert.NotNull(cl2_v2);
        }
    }
}