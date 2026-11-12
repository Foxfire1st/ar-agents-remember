# mcp/tests/test_paseo_role_answers_l111.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Check role payload projections and log readback with a fake host, including held-delivery and waited-reply seams.

## Code Commentary

Start fixtures check compact success fields, missing-requirement warnings and refused outcomes. Ordinary id-addressed messages have their own location-free size/shape assertion; role-addressed/cancelled deliveries separately pin recipient identity and warning. A fake host is not a real-provider delivery qualification.

The held-message fixture goes through `role_message_payload`, not just the product sender: a named permission, hold reason, issued id, queue counts and recipient survive delivery, and the whole detail retains the id. This addresses the projection seam that direct sender tests cannot witness. It is a named finite permission-hold case, not proof that every long held answer keeps its whole narrative in the bounded response.

Waited-reply cases preserve the beginning under the exception bound and read back the complete reply, with separate log-loss/late-line controls. None of these source cases decides a CODE round or the independent composition check.

## Evidence

- The held permission fixture checks delivered facts through the adapter and reads back the issued id. [1]
- Role addressing preserves recipient identity and host-cancellation warning. [2]
- The waited-reply fixture retains a bounded prefix and the whole reply in detail. [3]
