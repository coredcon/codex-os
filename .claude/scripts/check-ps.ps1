Write-Output "PS Version: $($PSVersionTable.PSVersion)"
Write-Output "PSEdition: $($PSVersionTable.PSEdition)"

# Check if AsTask exists
try {
    $methods = [System.WindowsRuntimeSystemExtensions].GetMethods()
    $asTaskMethods = $methods | Where-Object { $_.Name -eq 'AsTask' }
    Write-Output "AsTask methods found: $($asTaskMethods.Count)"
    foreach ($m in $asTaskMethods) {
        $params = $m.GetParameters() | ForEach-Object { $_.ParameterType.Name }
        Write-Output "  - params: $($params -join ', ')"
    }
} catch {
    Write-Output "WindowsRuntimeSystemExtensions error: $_"
}
