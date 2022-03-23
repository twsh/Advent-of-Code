-- local file = io.open( "test.txt", "r" ) -- 900
local file = io.open( "input.txt", "r" ) -- 1282809906
local horizontal = 0
local depth = 0
local aim = 0
for line in file:lines() do
	local instruction = string.gmatch(line, "%w+")
	local command = instruction()
	local value = tonumber(instruction())
	if command == "forward" then
		horizontal = horizontal + value
		depth = depth + (aim * value)
	elseif command == "down" then
		aim = aim + value
	elseif command == "up" then
		aim = aim - value
	end
end
print("horizontal: " .. horizontal)
print("depth: " .. depth)
print(horizontal * depth)
file:close()
