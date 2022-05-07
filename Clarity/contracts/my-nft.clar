;; use the SIP009 interface (testnet)
;; trait deployed by deployer address from ./settings/Devnet.toml
(impl-trait 'ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM.nft-trait.nft-trait)

;; define a new NFT. 
(define-non-fungible-token CirclyNFT uint)

;; Store the last issues token ID
(define-data-var last-token-id uint u0)

(define-public (mint)
    (nft-mint? CirclyNFT u1 tx-sender)
)

;; SIP009: Transfer token to a specified principal
(define-public (transfer (token-id uint) (sender principal) (recipient principal))
     (nft-transfer? CirclyNFT token-id sender recipient))



;; SIP009: Get the owner of the specified token ID
(define-read-only (get-owner (token-id uint))
  (ok (nft-get-owner? CirclyNFT token-id)))

;; SIP009: Get the last token ID
(define-read-only (get-last-token-id)
  (ok (var-get last-token-id)))

;; SIP009: The user can upload the generated picture and it's metadata into IPFS and then put it here
(define-read-only (get-token-uri (token-id uint))
  ;;(ok (some "https://gateway.pinata.cloud/ipfs/CI"))
   (ok none) ;;I chose not to put a URI
  )
