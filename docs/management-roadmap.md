# SMS Sender for Ethiopia — Management Roadmap

This document describes a possible future management layer. It is a planning artifact only: contacts, campaigns, sender IDs, web management, and the related API endpoints are not implemented in this phase.

## Product direction

Provide a small, self-hosted messaging workspace that manages contacts and approved message workflows, then sends through the existing Android device gateway. Keep the Android phone as the SMS transport and make the web interface an optional management client.

## Proposed capabilities

1. **Contacts**
   - Create, update, search, archive, import, and export contacts.
   - Store phone numbers in normalized international format and validate them before sending.
   - Support custom fields only where a concrete messaging need exists.
2. **Groups**
   - Organize contacts into named groups and preview recipient counts.
   - Prevent duplicate recipients when a contact belongs to multiple selected groups.
3. **Sender identity**
   - Show the Android device/SIM identity and its carrier-provided sender behavior.
   - Do not promise arbitrary sender-name masking; verify operator and device support before exposing sender-ID options.
4. **Messages and campaigns**
   - Compose a message, select contacts or groups, review a recipient summary, and confirm before sending.
   - Add reusable templates, personalization previews, scheduling, and delivery/error history in later increments.
   - Start with explicit user-triggered sends; add bulk sending only with clear rate limits, consent checks, and cancellation.
5. **Web management**
   - Offer an optional browser dashboard for contacts, groups, templates, and campaign history.
   - Keep the web client and Android gateway behind authenticated, encrypted connections; never expose the gateway directly to the public internet by default.
6. **API**
   - Preserve the existing send endpoint for compatibility.
   - Add versioned endpoints for contacts, groups, message previews, campaigns, and status only after their data model and authorization rules are agreed.
   - Use request validation, per-client credentials, rate limits, idempotency for campaign submission, and structured error responses.

## Suggested delivery phases

1. **Foundation** — confirm whether data stays on the phone or moves to a local server; define consent, retention, backup, and authentication requirements; document API compatibility.
2. **Contacts and groups** — implement local persistence, import/export, phone-number normalization, and recipient previews.
3. **Single-message workflow** — add templates, validation, explicit confirmation, send-result history, and cancellation/error states.
4. **Web dashboard and API** — add an authenticated management client and versioned management endpoints over a protected connection.
5. **Campaign operations** — add scheduling, controlled batches, progress, retries, and audit history after operational limits are tested.

## Decisions to settle before implementation

- Where contact and campaign data is stored and who can access it.
- Supported import formats, duplicate matching, and data-retention behavior.
- Consent and opt-out handling appropriate to the deployment.
- Per-device and per-carrier throughput limits, message length/segment estimates, and retry behavior.
- Whether remote web access is needed; if so, the hosting and secure connectivity model.
- Which Android versions, SIM configurations, and carrier sender-identity behaviors must be supported.

## Out of scope for the current UI refresh

No management database, contact editor, group editor, sender-name override, bulk campaign sender, web server/dashboard, or new management API endpoint is included. The current SMS send behavior and existing API contract remain unchanged.
