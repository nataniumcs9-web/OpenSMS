# SMS Sender for Ethiopia — SMS Management System Plan

This is the plan for building the SMS management system. It is a planning document only: contact management, campaigns, sender identity controls, web management, and related API endpoints have not been implemented yet.

## Product direction

Build a simple, self-hosted SMS management workspace for Ethiopian users. Manage contacts and approved messaging workflows, then send through a compatible Android phone and SIM. Keep the Android phone as the SMS transport and make a web dashboard an optional management client.

The product should be tested with Ethiopian Android devices, SIMs, and carrier services before claiming reliable local compatibility. Delivery, fees, sender identity, and throughput depend on the device and mobile operator.

## Proposed capabilities

1. **Contacts**
   - Create, update, search, archive, import, and export contacts.
   - Accept Ethiopia's `+251` international dialing format and normalize validated Ethiopian phone numbers consistently.
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
   - Evaluate Amharic and other language input, Unicode message segmentation, and accurate segment estimates on target Android devices and carrier networks.
   - Add reusable templates, personalization previews, scheduling, and delivery/error history in later increments.
   - Start with explicit user-triggered sends; add bulk sending only with clear rate limits, consent checks, and cancellation.
5. **Web management**
   - Offer an optional browser dashboard for contacts, groups, templates, and campaign history.
   - Keep the web client and Android gateway behind authenticated, encrypted connections; never expose the gateway directly to the public internet by default.
6. **API**
   - Preserve the existing send endpoint for compatibility.
   - Add versioned endpoints for contacts, groups, message previews, campaigns, and status only after their data model and authorization rules are agreed.
   - Use request validation, per-client credentials, rate limits, idempotency for campaign submission, and structured error responses.

## Build plan

1. **Ethiopian device and carrier validation** — test SMS send permissions, +251 number formats, language/Unicode messages, delivery results, and carrier limits across agreed target Android phones and SIMs.
2. **Product and data foundation** — choose phone-local versus local-server data storage; define consent, opt-out, retention, backup, authentication, and API compatibility requirements.
3. **Contacts and groups** — implement local persistence, import/export, Ethiopian number normalization, contact search, and accurate recipient previews.
4. **Single-message workflow** — add templates, language-aware previews, validation, explicit confirmation, send-result history, and useful failure feedback.
5. **Web dashboard and API** — add an authenticated management client and versioned contact/group/message endpoints over a protected connection.
6. **Campaign operations** — add scheduling, controlled batches, progress, retries, cancellation, and audit history after carrier and device limits are tested.

## Decisions to settle before implementation

- Where contact and campaign data is stored and who can access it.
- Ethiopian phone-number validation rules, supported import formats, duplicate matching, and data-retention behavior.
- Consent and opt-out handling appropriate to the deployment and applicable Ethiopian requirements.
- Supported Android versions, Ethiopian carrier/SIM combinations, SMS delivery confirmation, throughput limits, and retry behavior.
- Language requirements and how message length and Unicode segments are estimated.
- Whether remote web access is needed; if so, the hosting and secure connectivity model.
- Which carrier sender-identity behaviors are supported; do not offer sender-name overrides unless the carrier supports them.

## Out of scope for the current UI refresh

No management database, contact editor, group editor, sender-name override, bulk campaign sender, web server/dashboard, or new management API endpoint is included yet. The current SMS send behavior and existing API contract remain unchanged. Ethiopian operator compatibility and delivery reliability have not yet been validated.
