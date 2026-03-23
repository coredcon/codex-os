Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager,Windows.Media.Control,ContentType=WindowsRuntime]

function Await($Task) {
    $resultType = $Task.GetType().GetGenericArguments()[0]
    $methods = [System.WindowsRuntimeSystemExtensions].GetMethods()
    $asTask = $null
    foreach ($m in $methods) {
        if ($m.Name -eq 'AsTask' -and $m.GetParameters().Count -eq 1) {
            $p = $m.GetParameters()[0]
            if ($p.ParameterType.Name -like 'IAsyncOperation*') {
                $asTask = $m
                break
            }
        }
    }
    if ($null -eq $asTask) { throw "AsTask method not found" }
    $generic = $asTask.MakeGenericMethod($resultType)
    $netTask = $generic.Invoke($null, @($Task))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}

try {
    $mgr = Await ([Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager]::RequestAsync())
    $session = $mgr.GetCurrentSession()
    if ($null -ne $session) {
        $props = Await ($session.TryGetMediaPropertiesAsync())
        $info = $session.GetPlaybackInfo()
        Write-Output "$($props.Artist)|$($props.Title)|$($props.AlbumTitle)|$($session.SourceAppUserModelId)|$($info.PlaybackStatus)"
    } else {
        Write-Output "NONE"
    }
} catch {
    Write-Output "ERROR: $_"
}
