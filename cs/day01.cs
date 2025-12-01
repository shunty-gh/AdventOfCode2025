#!/usr/bin/env dotnet
#:project ./utils/aocutils.csproj

using Shunty.AoC;

AocUtils.PrintTitle($"Advent of Code {AocUtils.AoCYear}");

await new Day01().Solve();

public class Day01 : AocDaySolver
{
    public int DayNumber => 1;

    public string Title => "";

    public async Task Solve()
    {
        var input = AocUtils.FindInputFile(DayNumber);
        var lines = await File.ReadAllLinesAsync(input);

        var start = 50;
        var current = start;
        var part1 = 0;
        var part2 = 0;
        foreach (var line in lines)
        {
            var sign = line[0] == 'R' ? 1 : -1;
            var value = int.Parse(line.Trim()[1..]);

            var p2mod = value % 100;
            var p2inc = value / 100;

            if (sign > 0 && current + p2mod >= 100)
            {
                part2 += p2inc + 1;
            }
            else if (sign < 0 && current != 0 && current - p2mod <= 0)
            {
                part2 += p2inc + 1;
            }
            else
            {
                part2 += p2inc;
            }

            current += (sign * value);
            if (current % 100 == 0)
            {
                part1 += 1;
            }
            current = ((current % 100) + 100) % 100; // C# annoying % operator
        }

        this.ShowDayHeader();
        this.ShowDayResult(1, part1);
        this.ShowDayResult(2, part2);
    }
}
