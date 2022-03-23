local file = io.open( "input.txt", "r" )
local increases = 0
local last = nil
local pointer = 1
local measurements = {}
for line in file:lines() do
	table.insert(measurements, tonumber(line))
end
local length = #measurements
while pointer + 1 < length do
	local sum = measurements[pointer] + measurements[pointer + 1] + measurements[pointer + 2]
	if last and sum > last then
		increases = increases + 1
	end
	last = sum
	pointer = pointer + 1
end
print(increases) -- solution is 1523
file:close()
