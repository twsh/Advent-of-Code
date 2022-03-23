-- local file = io.open( "test.txt", "r" ) -- 198
local file = io.open( "input.txt", "r" ) -- 3912944
local gamma = ""
local epsilon = ""
local bits = nil
local line_length = nil

-- use the bits table to keep track of the number of 0 and 1 at each bit
for line in file:lines() do
	if not bits then
		line_length = #line
		bits = {}
		for i = 1, #line do
			bits[i] = {["0"] = 0, ["1"] = 0}
		end
	end
	for i = 1, #line do
		local bit = line:sub(i, i)
		bits[i][bit] = bits[i][bit] + 1
	end
end

-- make the gamma and epsilon
for i = 1, line_length do
	if bits[i]["0"] > bits[i]["1"] then
		gamma = gamma .. "0"
		epsilon = epsilon .. "1"
	else
		gamma = gamma .. "1"
		epsilon = epsilon .. "0"
	end
end

-- print("gamma: " .. gamma)
-- print("epsilon: " .. epsilon)


local function value(string)
	local out = 0
	local multiplier = 1
	for i = 1, #string do
		local pointer = #string + 1 - i
		local bit = string:sub(pointer, pointer)
		out = out + (tonumber(bit) * multiplier)
		multiplier = multiplier * 2
	end
	return out
end

print(value(gamma) * value(epsilon))
file:close()
