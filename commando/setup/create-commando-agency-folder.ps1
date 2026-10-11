# Creates the Commando Agency working folder on drive E:.
# How to run: right-click this file > "Run with PowerShell" (or paste it into a PowerShell window).
$root = "E:\Commando Agency"
$folders = @(
  "01 Leads\Egypt",
  "01 Leads\Gulf - Dubai",
  "02 Product References\Mayura Khamas Perfumes",
  "02 Product References\Inayah Abaya",
  "02 Product References\Adaa Lounge Perfumes",
  "02 Product References\R A M Perfumes",
  "03 AI Generations\Mayura Khamas\raw",
  "03 AI Generations\Mayura Khamas\final",
  "03 AI Generations\Tests (fictional products)",
  "04 Portfolio",
  "05 CV",
  "06 Clients\La Margrita",
  "06 Clients\Mr Rakha",
  "07 Playbooks"
)
foreach ($f in $folders) { New-Item -ItemType Directory -Force -Path (Join-Path $root $f) | Out-Null }
@"
How to fill 02 Product References (2 minutes per lead)
1. Open Google Maps, search the shop name + Dubai, click Photos.
2. Save the 2-3 clearest photos of their actual bottles/products into that lead's folder.
3. Name them: front.jpg, angle.jpg, label-closeup.jpg
4. If no clear product photo exists, skip that lead for AI samples.
Upload these as @product when generating.
"@ | Set-Content (Join-Path $root "02 Product References\README.txt")
Write-Host "Done: $root created."
explorer $root
