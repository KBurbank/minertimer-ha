# MinerTimer Home Assistant Integration

Control Minecraft playtime limits from Home Assistant

## Installation

### HACS (Recommended)

1. Make sure [HACS](https://hacs.xyz) is installed
2. Add this repository to HACS:
   - HACS → Integrations → ⋮ → Custom repositories
   - Add URL: `https://github.com/kburbank/minertimer-ha`
   - Category: Integration
3. Click "Download"
4. Restart Home Assistant
5. Add the integration:
   - Settings → Devices & Services → Add Integration
   - Search for "MinerTimer"

### Manual

1. Copy the `custom_components/minertimer` directory to your Home Assistant `custom_components` directory
2. Restart Home Assistant
3. Add the integration through the UI

## Configuration

The integration will automatically create:
- An input_number entity for time limits
- A sensor for tracking played time
- A daily reset automation

No additional configuration needed! 