local ok, mymod = pcall(require, 'module_with_error')
if not ok then
  print("Module had an error")
else
  mymod.function()
end
