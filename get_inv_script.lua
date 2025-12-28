local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Inventory = ReplicatedStorage:WaitForChild("Remotes"):WaitForChild("Inventory")
local HttpService = game:GetService("HttpService")

local Weapons = require(game:GetService("ReplicatedStorage").Database.Sync.Item)
--local Pets = require(game:GetService("ReplicatedStorage").Database.Sync.Pets)

local InventoryWithInfo = {
    ["Weapons"] = {},
    ["Pets"] = {}
}

local args = {
	"username"
}
local Inv = game:GetService("ReplicatedStorage"):WaitForChild("Remotes"):WaitForChild("Extras"):WaitForChild("GetFullInventory"):InvokeServer(unpack(args))

--writefile("Profile.txt", HttpService:JSONEncode(Inv))
--writefile("Weapons.txt", HttpService:JSONEncode(Weapons))
--writefile("Pets", HttpService:JSONEncode(Pets))

for i,v in pairs(Inv.Weapons.Owned) do
    local Data = Weapons[i]
    Data["Count"] = v
    InventoryWithInfo["Weapons"][i] = Data
end

for i,v in pairs(Inv.Pets.Owned) do
    local Data = {}
    Data["Count"] = v
    InventoryWithInfo["Pets"][i] = Data
end

writefile("Inventory.txt", HttpService:JSONEncode(InventoryWithInfo))