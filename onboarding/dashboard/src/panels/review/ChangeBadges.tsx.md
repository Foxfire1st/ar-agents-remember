# dashboard/src/panels/review/ChangeBadges.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render delivered member and family change facts as badges, secondary marks and visible reasons. The compact outline badge uses the same fact vocabulary without classifying source or changing a review judgment.

## Code Commentary

`useMemberChange` joins a returned member to the supplied fact map and any followed marker targeting that exact family/member revision. No supplied map produces no detailed badge; a supplied map missing the member produces the explicit undescribed unknown fact. Its accessible description orders change kind, change-kind reasons and membership even when the followed marker makes the membership line appear first.

`MemberChangeBadge` renders the supplied primary kind, every secondary mark and the complete labelled unknown reasons. `membershipLine` prefers the comparison's supplied unknown-membership reasons; otherwise an active marker supplies its own classification reason. The marker adds an Attribution unknown tag without replacing a known comparison fact. `UnknownReason` appends the curation explanation and keeps the supplied reasons visible.

`GuaranteeChangeBadge` describes the family's independently authored guarantee; `FamilyBreakdown` reports member-occurrence populations and partiality, rather than presenting those populations as an intent count. `OutlineChangeBadge` renders one worded primary badge with its meaning in the title; unknown has a dashed style, and an aggregate family badge names changed members while the family record itself is unchanged.

## Evidence

- ChangeBadges.tsx current behavior at this source owner. [23]
- ChangeBadges.tsx current behavior at this source owner. [24]
- ChangeBadges.tsx current behavior at this source owner. [25]
