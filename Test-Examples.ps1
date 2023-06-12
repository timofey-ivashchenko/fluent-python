param($Directory)

Clear-Host

Get-ChildItem -Path . -Filter *.doctest | ForEach-Object {
    $Output = & python -m doctest $_.Name

    if ([string]::IsNullOrEmpty($Output)) {
        Write-Host $_.Name -ForegroundColor Cyan -NoNewline
        Write-Host ' Test passed.' -ForegroundColor Green
    } else {
        $Color = $Host.UI.RawUI.ForegroundColor
        $Host.UI.RawUI.ForegroundColor = 'Red'
        & python -m doctest $_.Name
        $Host.UI.RawUI.ForegroundColor = $Color
    }
}
