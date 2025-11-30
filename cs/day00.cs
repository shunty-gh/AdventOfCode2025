#!/usr/bin/env dotnet
#:project ./utils/aocutils.csproj

using Shunty.AoC;

AocUtils.PrintTitle($"Advent of Code {AocUtils.AoCYear}");

await new Day00().Solve();

public class Day00 : AocDaySolver
{
    public int DayNumber => 0;

    public string Title => "";

    public async Task Solve()
    {
        var input = AocUtils.FindInputFile(DayNumber);
        var lines = await File.ReadAllLinesAsync(input);

        this.ShowDayHeader();
        this.ShowDayResult(1, "TODO Part 1");
        this.ShowDayResult(2, "TODO Part 2");
    }
}
