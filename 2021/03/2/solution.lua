-- local file = io.open( "test.txt", "r" ) -- 230
local file = io.open( "input.txt", "r" ) -- 4996233
local lines = {}

for line in file:lines() do
	table.insert(lines, line)
end

local function get_bits(list_of_lines)
	local bits = nil
	for i = 1, #list_of_lines do
		if not bits then
			bits = {}
			for j = 1, #lines[i] do
				bits[j] = {["0"] = 0, ["1"] = 0}
			end
		end
		local line = list_of_lines[i]
		for k = 1, #line do
			local bit = line:sub(k, k)
			bits[k][bit] = bits[k][bit] + 1
		end
	end
	return bits
end

--[[ local test = get_bits(lines)

for i = 1, #test do
	print(i .. ": 0: " .. test[i]["0"] .. "; 1: " .. test[i]["1"])
end ]]

local function filter(list_of_lines, bit, direction)
	local not_bit = nil
	if bit == "1" then
		not_bit = "0"
	elseif bit == "0" then
		not_bit = "1"
	end
	local filtered = list_of_lines
	local pointer = 1
	while #filtered > 1 do
		local bits = get_bits(filtered)
		local criteria = nil
		if direction == "greater" then
			if bits[pointer][bit] >= bits[pointer][not_bit] then
				criteria = bit
			else
				criteria = not_bit
			end
		elseif direction == "lesser" then
			if bits[pointer][bit] <= bits[pointer][not_bit] then
				criteria = bit
			else
				criteria = not_bit
			end
		end
		local new_filtered = {}
		for i = 1, #filtered do
			local line = filtered[i]
			local character = line:sub(pointer, pointer)
			if character == criteria then
				table.insert(new_filtered, line)
			end
		end
		filtered = new_filtered
		pointer = pointer + 1
	end
	return filtered[1]
end

local o2 = filter(lines, "1", "greater")
local co2 = filter(lines, "0", "lesser")

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

print("o2: " .. o2)
print("co2: " .. co2)
print("o2 * co2: " .. value(o2) * value(co2))

file:close()
