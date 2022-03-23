local file = io.open( "input.txt", "r" )
local increases = 0
local last = nil
for line in file:lines() do
	if last and tonumber(line) > last then
		increases = increases + 1
	end
	last = tonumber(line)
end
print(increases) -- solution is 1477
file:close()
