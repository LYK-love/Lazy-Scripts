-- local ok, mymod = pcall(require, 'module_with_error')
-- if not ok then
  -- print("Module had an error")
-- else
  -- mymod.function()
-- end
-- Different types

local x = 10 -- number
local name = "sid" -- string
local isAlive = true -- boolean
local a = nil --no value or invalid value

-- increment in numbers
local n = 1
n = n + 1
print(n) -- 2

-- strings
-- Concatenate strings
local phrase = "I am"
local name = "Sid"

print(phrase .. " " .. name) -- I am Sid
print("I am " .. "Sid")
