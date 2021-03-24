$Body = @{
    "item_id" = "123456"
	"rev_id" = "00"
}
$Response = Invoke-WebRequest 'http://127.0.0.1:5000/item_extract/rest' -Method POST -Body ($Body|ConvertTo-Json) -ContentType "application/json"
Write-Output $Response.Content