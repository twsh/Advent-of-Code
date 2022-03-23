-- local file = io.open( "test.txt", "r" ) -- 150
local file = io.open( "input.txt", "r" ) -- 1480518
local horizontal = 0
local depth = 0
for line in file:lines() do
	local instruction = {}
	for word in string.gmatch(line, "%w+") do
		table.insert(instruction, word)
	end
	if instruction[1] == "forward" then
		horizontal = horizontal + tonumber(instruction[2])
	elseif instruction[1] == "down" then
		depth = depth + tonumber(instruction[2])
	elseif instruction[1] == "up" then
		depth = depth - tonumber(instruction[2])
	end
end
print("horizontal: " .. horizontal)
print("depth: " .. depth)
print(horizontal * depth)
